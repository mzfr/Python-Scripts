import os

for filename in os.listdir("."):

    if filename.endswith(".mp3"):

        if filename.startswith(" -"):
            os.rename(filename,filename[2:])
            print("done")

        else:

            print("Nothing happen")
