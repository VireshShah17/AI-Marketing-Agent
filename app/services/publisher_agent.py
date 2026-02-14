import os


def publish_post(post):
    os.makedirs("published_posts", exist_ok = True)
    with open(f"published_posts/post_{post.id}.txt", "w") as f:
        f.write(f"Caption: {post.caption}\n")
        f.write(f"Image Path: {post.image_path}\n")
        f.write(f"Status: {post.status}\n")

    return True