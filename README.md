# euler

## Dependencies
- Python 2.7
- cement framework
- re
- pycurl

## Supported languages
- python
- ruby


## Example usage
To generate the templates for the euler problems in the subdirectory:
> python proeule.py --lang python --dir ./python


## Known Issues

- Sometimes the script stops with the message "problem content not found". This occurs whenever the HTML content hasnt finished loading but the script already finished looking for the description content within the not fully loaded document.
  Todo: check if document has finished loading.
-
