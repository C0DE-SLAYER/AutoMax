def user_listing_dir(instance, filename):
    return f"user_{instance.seller.user.id}/listing/{filename}"