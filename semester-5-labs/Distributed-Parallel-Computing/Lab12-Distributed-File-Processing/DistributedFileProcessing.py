
import multiprocessing
import os


def process_chunk(lines):
    """Process a chunk of lines and return its statistics."""
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    character_count = sum(len(line) for line in lines)

    return {
        "process_id": os.getpid(),
        "lines": line_count,
        "words": word_count,
        "characters": character_count
    }


def split_into_chunks(lines, number_of_chunks):
    """Divide lines into approximately equal-sized chunks."""
    chunks = []
    chunk_size = (len(lines) + number_of_chunks - 1) // number_of_chunks

    if chunk_size == 0:
        return chunks

    for start in range(0, len(lines), chunk_size):
        chunks.append(lines[start:start + chunk_size])

    return chunks


def main():
    filename = "input.txt"
    number_of_workers = 2

    print("=== Distributed File Processing ===")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: {filename} was not found.")
        return

    chunks = split_into_chunks(lines, number_of_workers)

    if not chunks:
        print("The input file is empty.")
        return

    print(f"Input file: {filename}")
    print(f"Total lines: {len(lines)}")
    print(f"Number of worker processes: {len(chunks)}")

    with multiprocessing.Pool(processes=len(chunks)) as pool:
        results = pool.map(process_chunk, chunks)

    total_lines = 0
    total_words = 0
    total_characters = 0

    print("\n--- Worker Results ---")

    for index, result in enumerate(results, start=1):
        print(
            f"Worker {index} (PID {result['process_id']}): "
            f"{result['lines']} lines, "
            f"{result['words']} words, "
            f"{result['characters']} characters"
        )

        total_lines += result["lines"]
        total_words += result["words"]
        total_characters += result["characters"]

    print("\n--- Combined Results ---")
    print(f"Total lines: {total_lines}")
    print(f"Total words: {total_words}")
    print(f"Total characters: {total_characters}")
    print("Distributed file processing completed.")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
