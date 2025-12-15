docker build -t jup_llm .

docker run -p 8888:8888 -v ./jupyter_data:/home/jovyan/work -v ~/.azure:/home/jovyan/.azure jup_llm

