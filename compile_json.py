import os
import json


def generate_directory_json(base_path):
    """
    Generates a JSON structure for directories that follow the
    '{style}/{source}/{experience}' hierarchy, counting only 'bongo_*.mid' files
    and including an experience level derived from the experience folder name.
    """
    # The root directory where the MIDI files are organized
    root_dir = os.path.join(base_path, 'assets/midi_organized_by_source_drums')
    data = []

    # Iterate over each style directory
    for style in sorted(os.listdir(root_dir)):
        style_path = os.path.join(root_dir, style)
        if os.path.isdir(style_path):
            style_dict = {'style': style, 'sources': []}

            # Iterate over each source directory within the style directory
            for source in sorted(os.listdir(style_path)):
                source_path = os.path.join(style_path, source)
                if os.path.isdir(source_path):
                    source_dict = {'name': source, 'experiences': []}

                    # Iterate over each experience directory within the source directory
                    for experience in sorted(os.listdir(source_path)):
                        experience_path = os.path.join(source_path, experience)
                        if os.path.isdir(experience_path):
                            # Filter and count only 'bongo_*.mid' files
                            bongo_files = [f for f in os.listdir(experience_path) if
                                           f.startswith('bongo_') and f.endswith('.mid')]
                            num_bongo_files = len(bongo_files) // 2

                            # Extract the experience level from the folder name, assuming format "experience_i"
                            exp_level = int(experience.split('_')[-1]) + 1
                            experience_dict = {
                                'experience': experience,
                                'num_files': num_bongo_files,
                                'experience_level': exp_level
                            }
                            source_dict['experiences'].append(experience_dict)

                    style_dict['sources'].append(source_dict)

            data.append(style_dict)

    return data


def main():
    base_path = '.'  # Set this to the path where your project is located
    directory_data = generate_directory_json(base_path)

    # Write the directory data to a JSON file
    with open(os.path.join(base_path, 'assets/data/sources.json'), 'w') as json_file:
        json.dump(directory_data, json_file, indent=4)

    return directory_data

if __name__ == "__main__":
    directory_data =  main()
