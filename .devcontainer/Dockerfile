# kaggleのpython環境をベースにする
FROM gcr.io/kaggle-images/python:v56

COPY requirements.txt /root/
WORKDIR /tmp/WORKDIR
# ライブラリの追加インストール
RUN pip install -U pip && \
    pip install fastprogress japanize-matplotlib

RUN python -m pip install jupyterlab



RUN pip install -r /root/requirements.txt