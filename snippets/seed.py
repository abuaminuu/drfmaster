from faker import Faker
from faker.providers import BaseProvider
import random

fake = Faker()

# 1. Define your custom code snippets
class CodeProvider(BaseProvider):
    def code_snippet(self):
        snippets = [
            'print("Hello, World!")',
            'console.log("Data loaded");',
            'System.out.println("Java is here");',
            'fmt.Println("Go snippet")',
            'def mock_func(): pass'
        ]
        return random.choice(snippets)

# 2. Add the provider to the Faker instance
fake.add_provider(CodeProvider)

# 3. Use it just like any other faker method
# print(fake.code_snippet())

from models import Snippet

snip = Snippet(
    title="Sample Snippet",
    code=fake.code_snippet(),
    linenos=True,
    language="Python",
    style="monokai"
)

# snip.save()



user_profile = {
    "name": fake.name(),
    "email": fake.email(),
    "address": fake.address(),
    "code": fake.code_snippet(),
    "job": fake.job(),
    "company": fake.company()
}

try:
    print(snip)
except Exception as e:
    raise f"Error: {e}"


# Title
# Code
# Linenos
# Language
# Style