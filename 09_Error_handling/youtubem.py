import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            data = json.load(file)
            # Validate that the loaded data is a list of dictionaries
            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                return data
            else:
                return []  # Reset to an empty list if the file content is invalid
    except FileNotFoundError:
        return []  # Return an empty list if the file does not exist

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file, indent=4)  # Added indent for better readability

def list_all_videos(videos):
    if not videos:
        print("\nNo videos found!")
        return

    print("\n")
    print("*" * 70)
    print("Listing all YouTube videos:")
    for index, video in enumerate(videos, start=1):
        # Validate each video entry before accessing keys
        if isinstance(video, dict) and 'name' in video and 'time' in video:
            print(f"{index}. {video['name']}, Duration: {video['time']}")
        else:
            print(f"{index}. [Invalid video data]")
    print("*" * 70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video duration (e.g., 10:25): ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print("\nVideo added successfully!")

def update_video(videos):
    if not videos:
        print("\nNo videos found to update!")
        return

    list_all_videos(videos)
    try:
        video_index = int(input("\nEnter the video number to update: ")) - 1
        if 0 <= video_index < len(videos):
            name = input("Enter new video name (leave blank to keep current): ")
            time = input("Enter new video duration (leave blank to keep current): ")
            if name:
                videos[video_index]['name'] = name
            if time:
                videos[video_index]['time'] = time
            save_data_helper(videos)
            print("\nVideo updated successfully!")
        else:
            print("\nInvalid video number!")
    except ValueError:
        print("\nInvalid input! Please enter a valid number.")

def delete_video(videos):
    if not videos:
        print("\nNo videos found to delete!")
        return

    list_all_videos(videos)
    try:
        video_index = int(input("\nEnter the video number to delete: ")) - 1
        if 0 <= video_index < len(videos):
            deleted_video = videos.pop(video_index)
            save_data_helper(videos)
            print(f"\nVideo '{deleted_video['name']}' deleted successfully!")
        else:
            print("\nInvalid video number!")
    except ValueError:
        print("\nInvalid input! Please enter a valid number.")

def main():
    videos = load_data()
    while True:
        print("\nYouTube Manager")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("\nEnter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("\nExiting the app. Goodbye!")
                break
            case _:
                print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()

