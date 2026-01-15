import random
import json
from faker import Faker
from faker.providers import BaseProvider

class CodeSnippetProvider(BaseProvider):
    """
    Custom Provider for generating structured programming code data.
    Updated for 2026 standards.
    """
    
    LANGUAGES = ['Python', 'JavaScript', 'TypeScript', 'Go', 'Rust', 'Java', 'C++', 'SQL']
    STYLES = ['monokai', 'github-dark', 'dracula', 'solarized-light', 'nord', 'one-dark']
    
    # Templates to generate dynamic code snippets
    SNIPPET_TEMPLATES = [
        ('Python', 'print("Hello, {name}!")'),
        ('JavaScript', 'console.log("Welcome to {city}");'),
        ('TypeScript', 'const user: string = "{name}";'),
        ('SQL', 'SELECT * FROM users WHERE city = "{city}";'),
        ('Go', 'fmt.Println("Deploying to {company}")'),
        ('Rust', 'println!("Memory safe code for {company}");')
    ]

    def language(self):
        return self.random.choice(self.LANGUAGES)

    def style(self):
        return self.random.choice(self.STYLES)

    def linenos(self):
        # Returns a random boolean for showing line numbers
        return self.random.choice([True, False])

    def code_data(self):
        """Generates a matching Language, Title, and Code snippet."""
        lang, template = self.random.choice(self.SNIPPET_TEMPLATES)
        
        # Use existing faker providers to fill templates
        name = self.generator.first_name()
        city = self.generator.city()
        company = self.generator.company()
        
        code = template.format(name=name, city=city, company=company)
        title = f"{lang} {self.random.choice(['Script', 'Utility', 'Snippet', 'Helper'])}"
        
        return {
            "title": title,
            "code": code,
            "language": lang
        }

# Initialize Faker
fake = Faker()
fake.add_provider(CodeSnippetProvider)

# Generate 100 snippets
snippets = []
for _ in range(100):
    # Combine fixed fields with dynamic ones from the provider
    dynamic_fields = fake.code_data()
    snippet = {
        "title": dynamic_fields["title"],
        "code": dynamic_fields["code"],
        "linenos": fake.linenos(),
        "language": dynamic_fields["language"],
        "style": fake.style()
    }
    snippets.append(snippet)

# Preview the first 3
print(json.dumps(snippets[:3], indent=2))
