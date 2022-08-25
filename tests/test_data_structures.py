from dataclasses import dataclass
from typing import TypedDict


@dataclass
class MovieAsDataClass:
    name: str
    year: int


def test_data_class() -> None:
    movie = MovieAsDataClass("Blade Runner", 1982)
    assert movie.name == "Blade Runner"
    assert movie.year == 1982


def test_data_class_named_arguments() -> None:
    movie = MovieAsDataClass(name="Blade Runner", year=1982)
    assert movie.name == "Blade Runner"
    assert movie.year == 1982


class MovieType(TypedDict):
    name: str
    year: int


def test_structural_typing() -> None:
    movie: MovieType = {"name": "Blade Runner", "year": 1982}
    assert movie["name"] == "Blade Runner"
    assert movie["year"] == 1982
