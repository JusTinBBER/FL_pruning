import flwr as fl

if __name__ == "__main__":
    while(True):
        fl.server.start_server(server_address="127.0.0.1:12345", config=fl.server.ServerConfig(num_rounds=3))
        