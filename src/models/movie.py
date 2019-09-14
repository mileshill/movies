from flask_restplus import fields

MOVIE = {
    "title": fields.String(
        description="Movie title",
        required=False
    ),
    "year": fields.Integer(
        description="Release year",
        required=False
    ),
    "cast": fields.List(
        fields.String(
            description="Cast members"
        )
    )
}
