#how to use (assuming the name: announcechanger2.py):

#to remove the announce:

#python3 announcechanger2.py -i /path/to/folder/with/original/.torrent/files -r -od /path/to/output/folder

#to change the announce:

#python3 announcechanger2.py -i /path/to/folder/with/original/.torrent/files -a announceurl -od /path/to/output/folder 

import argparse
import bencodepy
import os
 
def process_torrent_file(input_torrent_path, announce_url, output_directory, remove_announce):
    # Read the existing torrent file
    with open(input_torrent_path, 'rb') as f:
        torrent_data = bencodepy.decode(f.read())
 
    # Modify or remove the announce URL
    if remove_announce:
        torrent_data.pop(b'announce', None)
        print(f"Announce URL removed from '{input_torrent_path}'")
    else:
        torrent_data[b'announce'] = announce_url.encode('utf-8')
        print(f"Announce URL '{announce_url}' added to '{input_torrent_path}'")
 
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)
 
    # Determine the output file path
    output_torrent_path = os.path.join(output_directory, os.path.basename(input_torrent_path))
 
    # Save the modified torrent file
    with open(output_torrent_path, 'wb') as f:
        f.write(bencodepy.encode(torrent_data))
 
    print(f"Modified torrent saved to '{output_torrent_path}'")
 
def process_folder(folder_path, announce_url, output_directory, remove_announce):
    # Iterate through the folder and process each .torrent file
    for filename in os.listdir(folder_path):
        if filename.endswith('.torrent'):
            input_torrent_path = os.path.join(folder_path, filename)
            process_torrent_file(input_torrent_path, announce_url, output_directory, remove_announce)
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add or remove an announce URL to/from .torrent files without rehashing.')
    parser.add_argument('-i', '--input', required=True, help='Path to the input .torrent file or folder')
    parser.add_argument('-a', '--announce', help='Announce URL to add (omit if removing announce URL)')
    parser.add_argument('-od', '--output_dir', required=True, help='Output directory for the modified .torrent file(s)')
    parser.add_argument('-r', '--remove', action='store_true', help='Remove the announce URL instead of adding one')
 
    args = parser.parse_args()
 
    # Check if input is a file or folder
    if os.path.isfile(args.input):
        # Single torrent file
        process_torrent_file(args.input, args.announce, args.output_dir, args.remove)
    elif os.path.isdir(args.input):
        # Folder of torrent files
        process_folder(args.input, args.announce, args.output_dir, args.remove)
    else:
        print("Error: The input path is not valid. Please provide a valid file or folder path.")
 
 