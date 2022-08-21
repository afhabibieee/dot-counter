FROM python:3.8.10

CMD mkdir /gui_dotcounter
COPY . /gui_dotcounter

WORKDIR /gui_dotcounter

EXPOSE 8501

RUN pip3 install -r requirements.txt

CMD streamlit run app.py