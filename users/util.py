def user_upload_dir(instance, filename):
    return f"user_{instance.user.id}/{filename}"