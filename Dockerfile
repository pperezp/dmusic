FROM archlinux
WORKDIR "/home/dmusic"
RUN pacman -Syu --noconfirm
RUN pacman -S --noconfirm bash git ffmpeg python python-pip nano
COPY main.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
