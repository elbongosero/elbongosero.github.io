---
layout: page
title: Genre Classifier Model
permalink: /further_analysis/genre_classifier_model/
description: 
nav: false
nav_order: 1000
horizontal: false
---

<br/><br/>

# **Introduction**
---

We trained a genre classifier model. The classifier architecture is shown below:

<img src="{{ site.baseurl }}/assets/additional/GenreClassifierArchitecture.png" alt="Confusion Matrix" style="width: 500px;"/>


The hyperparameters used for training the model are as follows:

```yaml
Encoder:
        n_layers: 5
        n_heads: 8
        embedding_dim: 128
        ffn_dim: 256
        n_genres: 9
        
```

<br/><br/>

## **Validation**
---

The model obtained an F1 score of 0.93 on the validation set. The confusion matrix is shown below:

<img src="{{ site.baseurl }}/assets/additional/GenreConfusionMatrix.png" alt="Confusion Matrix" style="width: 500px;"/>


<br/><br/>

## **Download** 
---

[GenreClassifier Model](/assets/additional/trained_models/genre_classifier.pth){: .btn}

<br/><br/>

## **Load Model**
---

You can load the model similar to the generative models

```python
import torch
from model import GenreClassifier
 
def load_model(model_path, model_class, params_dict=None, is_evaluating=True, device=None):
    try:
        if device is not None:
            loaded_dict = torch.load(model_path, map_location=device)
        else:
            loaded_dict = torch.load(model_path)
    except:
        loaded_dict = torch.load(model_path, map_location=torch.device('cpu'))

    if params_dict is None:
        if 'params' in loaded_dict:
            params_dict = loaded_dict['params']
        else:
            raise Exception(f"Could not instantiate model as params_dict is not found. "
                            f"Please provide a params_dict either as a json path or as a dictionary")

    if isinstance(params_dict, str):
        import json
        with open(params_dict, 'r') as f:
            params_dict = json.load(f)

    model = model_class(params_dict)
    model.load_state_dict(loaded_dict["model_state_dict"])
    if is_evaluating:
        model.eval()

    return model
    
model_genre_classifier = load_model("path/to/genre_classifier.pth", GenreClassifier)

```

<br/><br/>

## **Usage**
---

```python
import torch

# prepare input
drum_hits = torch.rand((1, 32, 9))    # 9 for kick, snare, closed hat, open hat, low tom, mid tom, high tom, crash, ride
drum_hits = torch.where(drum_hits > 0.5, torch.tensor(1.0), torch.tensor(0.0))
drum_velocities = torch.rand((1, 32, 9)) * drum_hits
drum_offsets = (torch.rand((1, 32, 9)) - 0.5) * drum_hits
drum_hvo = torch.cat([drum_hits, drum_velocities, drum_offsets], dim=-1)

# predict
genre_ix, genre_probs = model_classifier.predict(drum_hvo)

# genre_ix is the predicted genre index corresponding to ['Afro', 'Disco', 'Funk', 'Hip-Hop/R&B/Soul', 'Jazz', 'Latin', 'Pop', 'Reggae', 'Rock']
# genre_probs is the predicted probabilities for each genre

```