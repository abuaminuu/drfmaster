import os
import sys
import random
from faker import Faker
from faker.providers import BaseProvider

# Get the current directory and parent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add both current and parent directories to the path
sys.path.append(parent_dir)
sys.path.append(current_dir)

# Get the current directory and parent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)  # Go up one level from snippets folder

# Add the project root to sys.path
sys.path.insert(0, project_root)

# 1. SET THE SETTINGS MODULE (Crucial)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drfmaster.settings')

# 2. INITIALIZE DJANGO
import django
django.setup()

# Now import Django models AFTER setup
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

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

def seed_data():

    # Create in smaller batches for SQLite
    batch_size = 50
    total_records = 100
    
    for batch_start in range(0, total_records, batch_size):
        batch_end = min(batch_start + batch_size, total_records)
        
        # code=fake.text(),
        id = [1,2,3]
        objs = [
            Snippet(
                owner_id = fake.random(),
                title=fake.catch_phrase(),
                code=fake.code_snippet(),
                linenos=fake.boolean(),
                language=random.choice([l[0] for l in LANGUAGE_CHOICES]),
                style=random.choice([s[0] for s in STYLE_CHOICES])
            )
            for _ in range(batch_start, batch_end)
        ]

        for o in objs:
            print("## ", o.code)
        print(len(objs))
        # try:
        #     Snippet.objects.bulk_create(objs)
        # except Exception as e:
        #     print(f"check: {e}")
        # print(f"Created {batch_end} records...")
    
    print("100 realistic entries generated.")


def create_fake_snippets(num_records):
    """Create fake snippets without using bulk_create"""
    
    languages = [lang[0] for lang in LANGUAGE_CHOICES]
    styles = [style[0] for style in STYLE_CHOICES]
    
    print(f"Creating {num_records} fake snippets...")
    # code=fake.text(max_nb_chars=500),
    id = [1,2,3]
    for i in range(num_records):
        try:
            # Create a snippet
            snippet = Snippet(
                owner_id = random.choice(id),
                title=fake.sentence(nb_words=4)[:100],  # Limit to 100 chars
                code=fake.code_snippet(),
                linenos=fake.boolean(),
                language=random.choice(languages),
                style=random.choice(styles)
            )
            
            # ** Save it individually
            snippet.save()
            # print(snippet.code)
            # Show progress
            if (i + 1) % 10 == 0:
                print(f"Created {i + 1} snippets...{snippet}")
                
        except Exception as e:
            print(f"Error creating snippet {i+1}: {e}")
            continue
    
    # Show final count
    count = Snippet.objects.count()
    print(f"\n✅ Done! Created {count} snippets in database.")


def gen_data():
    for _ in range(10):
        print(fake.first_name())

    id = [1,3,2]
    print(random.choice(id))


if __name__ == "__main__":
    # gen_data()
    # seed_data()
    create_fake_snippets(150)
    pass
