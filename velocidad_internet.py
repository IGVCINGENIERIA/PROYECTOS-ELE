import speedtest


def medir_velocidad():
    st = speedtest.Speedtest(secure=True)
    st.get_best_server()
    descarga = st.download() / 1_000_000
    carga = st.upload() / 1_000_000
    print(f"Velocidad de descarga: {descarga:.2f} Mbps")
    print(f"Velocidad de carga: {carga:.2f} Mbps")


if __name__ == "__main__":
    medir_velocidad()
