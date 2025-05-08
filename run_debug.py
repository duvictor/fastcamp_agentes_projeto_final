"""
utilizado como alternativa para facilitar o debug do ambiente streamlit
"""

from streamlit.web.bootstrap import run

real_script = 'app.py'
run(real_script, False, [], {})