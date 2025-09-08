## Code Wars kata solutions

### Create virtual environment
`$ python3 -m venv .venv`

### Activate virtual environment
`$ source .venv/bin/activate`

### Deactivate virtual environment
`$ deactivate`

### Install packages from requirements.txt
`$ pip install -r requirements.txt`

### For juypter notebook
`$ pip install jupyter ipykernel`

Register the Virtual Environment as a Jupyter Kernel:

This step makes your virtual environment available as a selectable kernel within Jupyter Notebook.

`$ python -m ipykernel install --user --name=pandas --display-name="Py3.13"`

### Run unittests in kyu folder
`$ python -m unittest tests/test_<name_of_file>.py`
