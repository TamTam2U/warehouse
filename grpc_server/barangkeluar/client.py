import barangkeluar_pb2_grpc as barangkeluar_pb2_grpc
import barangkeluar_pb2 as barangkeluar_pb2
import grpc


class BarangKeluarClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5003

        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = barangkeluar_pb2_grpc.BarangKeluarServiceStub(self.channel)

    def list_barangkeluar(self):
        res = self.stub.list(barangkeluar_pb2.BarangKeluarListRequest())

        if len(res.barangkeluar) == 0:
            return None

        return [
            dict(
                id=barangkeluar.id,
                item=barangkeluar.item,
                tanggalKeluar=barangkeluar.tanggalKeluar,
                supplierID=barangkeluar.supplierID,
                qty=barangkeluar.qty,
            )
            for barangkeluar in res.barangkeluar
        ]

    def get_barangkeluar(self, id):
        res = self.stub.get(barangkeluar_pb2.BarangKeluarDetailRequest(id=id))

        if res is None:
            return None

        return dict(
            id=res.barangkeluar.id,
            item=res.barangkeluar.item,
            tanggalKeluar=res.barangkeluar.tanggalKeluar,
            supplierID=res.barangkeluar.supplierID,
            qty=res.barangkeluar.qty,
        )

    def create_barangkeluar(self, item, tanggalKeluar, supplierID, qty):
        res = self.stub.create(
            barangkeluar_pb2.BarangKeluarCreateRequest(
                item=item,
                tanggalKeluar=tanggalKeluar,
                supplierID=supplierID,
                qty=int(qty),
            )
        )

        if res is None:
            return None

        return dict(
            id=res.barangkeluar.id,
            item=res.barangkeluar.item,
            tanggalKeluar=res.barangkeluar.tanggalKeluar,
            supplierID=res.barangkeluar.supplierID,
            qty=res.barangkeluar.qty,
        )

    def update_barangkeluar(self, id, item, tanggalKeluar, supplierID, qty):
        res = self.stub.update(
            barangkeluar_pb2.BarangKeluarUpdateRequest(
                id=int(id),
                item=item,
                tanggalKeluar=tanggalKeluar,
                supplierID=supplierID,
                qty=int(qty),
            )
        )

        if res is None:
            return None

        return dict(
            id=res.barangkeluar.id,
            item=res.barangkeluar.item,
            tanggalKeluar=res.barangkeluar.tanggalKeluar,
            supplierID=res.barangkeluar.supplierID,
            qty=res.barangkeluar.qty,
            message="Barang Keluar updated successfully",
        )
    
    def delete_barangkeluar(self, id):
        res = self.stub.delete(barangkeluar_pb2.BarangKeluarDeleteRequest(id=int(id)))

        if res is None:
            return None

        return dict(
            message="Barang Keluar deleted successfully",
        )


if __name__ == "__main__":
    while True:
        print("1. List Barang Keluar")
        print("2. Get Barang Keluar")
        print("3. Create Barang Keluar")
        print("4. Update Barang Keluar")
        print("5. Delete Barang Keluar")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == "1":
            client = BarangKeluarClient()
            print(client.list_barangkeluar())
        elif pilihan == "2":
            id = input("Masukkan ID: ")
            client = BarangKeluarClient()
            print(client.get_barangkeluar(int(id)))
        elif pilihan == "3":
            item = input("Masukkan item: ")
            tanggalKeluar = input("Masukkan tanggal keluar: ")
            supplierID = input("Masukkan supplier ID: ")
            qty = input("Masukkan qty: ")
            client = BarangKeluarClient()
            print(client.create_barangkeluar(item, tanggalKeluar, supplierID, qty))
        elif pilihan == "4":
            id = input("Masukkan ID: ")
            item = input("Masukkan item: ")
            tanggalKeluar = input("Masukkan tanggal keluar: ")
            supplierID = input("Masukkan supplier ID: ")
            qty = input("Masukkan qty: ")
            client = BarangKeluarClient()
            print(client.update_barangkeluar(id, item, tanggalKeluar, supplierID, qty))
        elif pilihan == "5":
            id = input("Masukkan ID: ")
            client = BarangKeluarClient()
            print(client.delete_barangkeluar(int(id)))
        else:
            break
