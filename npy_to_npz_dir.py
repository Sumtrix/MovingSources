import numpy as np
import os

def npy_to_npz_in_directory(input_directory, output_directory=None):
    """
    Converts all .npy files in a given directory to .npz files and saves them.

    Args:
        input_directory (str): Directory containing .npy files to be converted.
        output_directory (str, optional): Directory to save the .npz files.
                                         Defaults to the same directory as the input files.

    Returns:
        list: Paths to the saved .npz files.
    """
    if output_directory is None:
        output_directory = input_directory

    npz_file_paths = []

    for file_name in os.listdir(input_directory):
        if file_name.endswith(".npy"):
            npy_file_path = os.path.join(input_directory, file_name)
            base_name = os.path.splitext(file_name)[0]
            npz_file_path = os.path.join(output_directory, f"{base_name}.npz")

            data = np.load(npy_file_path)
            np.savez(npz_file_path, data=data)
            npz_file_paths.append(npz_file_path)
            print(f"Converted {npy_file_path} to {npz_file_path}")

    return npz_file_paths

# Example usage
if __name__ == "__main__":
    #input_dir = "/Users/johannesrolfes/Downloads/AW__Git-Branch/SNR-3dB_LE"  # Replace with the actual path
    #output_dir = "/Users/johannesrolfes/Downloads/AW__Git-Branch/LE_Modell_-3"  # Optional, specify output directory if needed
    input_dir = "/Users/johannesrolfes/Downloads/AW__Git-Branch/SNR-7dB_LE"
    output_dir = "/Users/johannesrolfes/Downloads/AW__Git-Branch/LE_Modell_-7"  # Optional, specify output directory if needed

    npy_to_npz_in_directory(input_dir, output_dir)
