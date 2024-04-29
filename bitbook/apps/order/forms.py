from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class Vegetable(FlaskForm):
    gar = IntegerField(
        "마늘 (kg단위)",
        validators=[
            DataRequired("수량 입력은 필수입니다."),
        ]
    )
    oni = IntegerField(
        "양파 (kg단위)",
        validators=[
            DataRequired("수량 입력은 필수입니다.")
        ]
    )
    car = IntegerField(
        "당근 (kg단위)",
        validators=[
            DataRequired("수량 입력은 필수입니다.")
        ]
    )