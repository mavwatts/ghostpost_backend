from rest_framework import serializers
from ghost_post_app.models import BoastRoast

class BoastRoastSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoastRoast
        fields = [
            "id",
            "choices",
            "user_input",
            "upvotes",
            "downvotes",
            "timeposted"
        ]