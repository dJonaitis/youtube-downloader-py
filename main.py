from pytube import YouTube

path = "./videos"

def main():

    link = input("Enter url:")

    video = YouTube(link)

    print("Title: ", video.title)
    print("Author: ", video.author)

    confirmation = input("Do you want to download this video? y/n ")

    if confirmation.lower() == 'y':
        print("Beginning download")
        videoStream = video.streams.filter(progressive=True).get_highest_resolution()
        videoStream.download(output_path = path, filename = f"{video.title}.mp4")
        print("Done downloading!")
    else:
        print("Let's find a new video to download!")
        main()
main()