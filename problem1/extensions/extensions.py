def main():
    message = input("File extension: ")
    print(mimetype(message))


def mimetype(message: str):
    totalParts = message.strip().lower().rsplit(".", 1)

    if len(totalParts) < 2:
        return "application/octet-stream"

    _, ext = message.strip().lower().rsplit('.', 1)
    match ext:
        case "gif":
            return "image/gif"
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"


main()
