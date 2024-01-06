"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, title, prompts, template):
        """Create story with words and template text."""
        self.title = title
        self.prompts = prompts
        self.template = template

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


normal_story = Story(
    "Normal story",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)


supergirl_story = Story(
    "Supergirl story",
    ["place", "noun", "verb", "plural_noun"],
    """{noun} {verb} {place} from {plural_noun}."""
)



superhero_story = Story(
    "Superhero story",
    ["noun", "first_adjective", "second_adjective"],
    """{noun} is {first_adjective} and {second_adjective}."""
)



christmas_story = Story(
    "Christmas story",
    ["adverb", "noun", "verb", "plural_noun", "subject"],
    """{adverb} of {noun}, we will {verb} {plural_noun} to {subject}."""
)

story_templates = {s.title: s for s in [normal_story, supergirl_story,
                    superhero_story, christmas_story]}
