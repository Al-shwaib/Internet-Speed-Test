import speedtest

def test_internet_speed():
    st = speedtest.Speedtest()
    
    print("Selecting the best server...")
    st.get_best_server()
    
    print("Measuring download speed...")
    download_speed = st.download() / 1_000_000  
    
    print("Upload speed is being measured...")
    upload_speed = st.upload() / 1_000_000 
    
    print("(Ping)...")
    ping = st.results.ping

    print(f"Download speed: {download_speed:.2f} Mbps")
    print(f"Lifting speed: {upload_speed:.2f} Mbps")
    print(f"Response time (Ping): {ping:.2f} ms")

if __name__ == "__main__":
    test_internet_speed()
