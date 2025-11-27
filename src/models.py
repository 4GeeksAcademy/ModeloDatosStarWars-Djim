from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(320), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorites: Mapped[List["Favorites"]] = relationship(back_populates='user')

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }


class People(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    gender: Mapped[str] = mapped_column(String(120),  nullable=False)
    hair_color: Mapped[str] = mapped_column(String(50), nullable=False)
    eye_color: Mapped[str] = mapped_column(String(100), nullable=False)
    height: Mapped[str] = mapped_column(String(120), nullable=False)
    mass: Mapped[str] = mapped_column(String(60), nullable=False)
    skin_color: Mapped[str] = mapped_column(String(40), nullable=False)
    favorites: Mapped[List["Favorites"]] = relationship(back_populates='people')


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.skin_color,
            
        }
    

class Planet(db.Model): 
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    climate: Mapped[str] = mapped_column(String(100), nullable=False)
    diameter: Mapped[str] = mapped_column(String(120), nullable=False)
    gravity: Mapped[str] = mapped_column(String(120), nullable=False)
    orbital_period: Mapped[str] = mapped_column(String(120), nullable=False)
    rotation_period: Mapped[int] = mapped_column(String(120), nullable=False)
    terrain: Mapped[int] = mapped_column(String(120), nullable=False)
    favorites: Mapped[List["Favorites"]] = relationship(back_populates='planet')


    def serialize(self):
        return { "id": self.id,
                 "name": self.name,
                 "climate": self.climate,
                 "diameter": self.diameter,
                 "gravity": self.gravity,
                 "orbital_period": self.orbital_period,
                 "rotation_period": self.rotation_period,
                 "terrain": self.terrain,


        }

class Favorites(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int] = mapped_column(ForeignKey("user.id"),primary_key=True)
    id_people: Mapped[int] = mapped_column(ForeignKey("people.id"),primary_key=True)
    id_planet: Mapped[int] = mapped_column(ForeignKey("planet.id"),primary_key=True)
