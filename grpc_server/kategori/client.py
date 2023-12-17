import kategori_pb2_grpc as kategori_pb2_grpc
import kategori_pb2 as kategori_pb2
import grpc

class KategoriClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5007
        
        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = kategori_pb2_grpc.KategoriServiceStub(self.channel)
    
    def list_kategori(self):
        request = kategori_pb2.KategoriListRequest()
        response = self.stub.list(request)
        
        if len(response.kategori) == 0:
            return None
        
        return [
            dict(
                id = kategori.id,
                kategori = kategori.kategori
            )
            for kategori in response.kategori
        ]

    def get_kategori(self, id):
        request = kategori_pb2.KategoriDetailRequest(id=id)
        response = self.stub.get(request)
        
        if response.kategori is None:
            return None
        
        return dict(
            id = response.kategori.id,
            kategori = response.kategori.kategori
        )

    def create_kategori(self, kategori):
        request = kategori_pb2.KategoriCreateRequest(kategori=kategori)
        response = self.stub.create(request)
        
        if response.kategori is None:
            return None
        
        return dict(
            id = response.kategori.id,
            kategori = response.kategori.kategori
        )
    
    def update_kategori(self, id, kategori):
        request = kategori_pb2.KategoriUpdateRequest(id=id, kategori=kategori)
        response = self.stub.update(request)
        
        if response.kategori is None:
            return None
        
        return dict(
            id = response.kategori.id,
            kategori = response.kategori.kategori
        )
    
    def delete_kategori(self, id):
        request = kategori_pb2.KategoriDeleteRequest(id=id)
        response = self.stub.delete(request)
        
        if response.message is None:
            return None
        
        return dict(
            message = response.message
        )

if __name__ == "__main__":
    while True:
        print("Kategori")
        print("1. List Kategori")
        print("2. Get Kategori")
        print("3. Create Kategori")
        print("4. Update Kategori")
        print("5. Delete Kategori")
        print("0. Exit")

        menu = input("Pilih menu> ")

        if menu == "1":
            kategori = KategoriClient()
            listK = kategori.list_kategori()
            print(listK)

        elif menu == "2":
            id = input("Id: ")
            kategori = KategoriClient()
            print(kategori.get_kategori(int(id)))

        elif menu == "3":
            kategoriS = input("Kategori: ")
            kategori = KategoriClient()
            print(kategori.create_kategori(kategoriS))

        elif menu == "4":
            id = input("Id: ")
            kategoriS = input("Kategori: ")
            kategori = KategoriClient()
            print(kategori.update_kategori(int(id), kategoriS))

        elif menu == "5":
            id = input("Id: ")
            kategori = KategoriClient()
            print(kategori.delete_kategori(int(id)))

        elif menu == "0":
            break