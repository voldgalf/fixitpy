"""FixitPy package."""

from .guides import retrieve_guide, retrieve_media

__all__ = ["retrieve_guide", "retrieve_media"]

if __name__ == "__main__":

    found_media = retrieve_media(14)
    print(found_media)

    found_guide = retrieve_guide(123,
                                 get_prerequisites=True)  # call the retrieve_guide function which returns a dict

    print(found_guide.get("title"))
    print(found_guide.get("difficulty"))

    for step in found_guide.get("steps"):
        print(step.get("title"))
        print(step.get("steps"))
