import nbformat as nbf
import re

def create_notebook():
    # Create a new notebook
    nb = nbf.v4.new_notebook()
    
    # Read the Python file
    with open('python_intermediate.py', 'r') as f:
        content = f.read()
    
    # Split the content into sections
    sections = content.split('# =====')
    
    # Process each section
    cells = []
    
    for section in sections:
        if not section.strip():
            continue
            
        # Get section number and title
        match = re.match(r'\s*(\d+)\.\s+(.*?)\s*=====', section)
        if match:
            section_num, section_title = match.groups()
            
            # 1. Section title as markdown
            cells.append(nbf.v4.new_markdown_cell(f"# {section_num}. {section_title}"))
            
            # 2. Description as markdown (before # Examples)
            description = section.split('# Examples')[0].strip()
            description = re.sub(r'^\s*\d+\.\s+.*?\s*=====\s*', '', description, flags=re.MULTILINE)
            description = re.sub(r'^#\s*', '', description, flags=re.MULTILINE)
            if description.strip():
                cells.append(nbf.v4.new_markdown_cell(description.strip()))
            
            # 3. Examples as code cell
            if '# Examples' in section:
                examples_part = section.split('# Examples')[1]
                if '# Practice Question' in examples_part:
                    examples = examples_part.split('# Practice Question')[0].strip()
                else:
                    examples = examples_part.strip()
                # Remove comments and stray numbers
                examples = re.sub(r'^#.*$', '', examples, flags=re.MULTILINE)
                examples = re.sub(r'^\d+\s*$', '', examples, flags=re.MULTILINE)
                if examples.strip():
                    cells.append(nbf.v4.new_markdown_cell("## Example"))
                    cells.append(nbf.v4.new_code_cell(examples.strip()))
            
            # 4. Practice Question as code cell
            if '# Practice Question' in section:
                practice = section.split('# Practice Question')[1].strip()
                # Remove comments and stray numbers
                practice = re.sub(r'^#.*$', '', practice, flags=re.MULTILINE)
                practice = re.sub(r'^\d+\s*$', '', practice, flags=re.MULTILINE)
                if practice.strip():
                    cells.append(nbf.v4.new_markdown_cell("## Practice"))
                    cells.append(nbf.v4.new_code_cell(practice.strip()))
    
    # Add all cells to the notebook
    nb['cells'] = cells
    
    # Write the notebook to a file
    with open('python_intermediate.ipynb', 'w') as f:
        nbf.write(nb, f)

if __name__ == '__main__':
    create_notebook() 