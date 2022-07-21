# function to check file type
def validateExtension(extensionType: str):
    # validates if Filename has an extension
    if extensionType.count(".") == 1:
        # matches the usecase of the extension
        match extensionType.split(".")[1]:
            case "gif":
                print("image/gif")
            case "jpg" | "jpeg":
                print("image/jpeg")
            case "png":
                print("image/png")
            case "pdf":
                print("application/pdf")
            case "txt":
                print("text/plain")
            case "zip":
                print("application/zip")
            case _:
                print("application/octet-stream")
    else: print("application/octet-stream")

# Main program asking file extension
def main():
    myFile = str(input("File Name: ")).lower()
    validateExtension(myFile)

# run program
main()