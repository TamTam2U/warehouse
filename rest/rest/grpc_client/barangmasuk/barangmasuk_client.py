import rest.grpc_client.barangmasuk.barangmasuk_pb2_grpc as barangkeluar_pb2_grpc
import rest.grpc_client.barangmasuk.barangmasuk_pb2 as barangkeluar_pb2
import grpc

class BarangMasukClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5004
        
        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = barangkeluar_pb2_grpc.BarangMasukServiceStub(self.channel)
    
    def list_barangmasuk(self):
        request = barangkeluar_pb2.BarangMasukListRequest()
        response = self.stub.list(request)
        
        if response is None:
            return None
        
        return[
            dict(
                id = barangmasuk.id,
                item = barangmasuk.item,
                tanggalMasuk = barangmasuk.tanggalMasuk,
                supplierID = barangmasuk.supplierID,
                qty = barangmasuk.qty,
            )
            for barangmasuk in response.barangmasuk
        ]
    
    def get_barangmasuk(self, id):
        request = barangkeluar_pb2.BarangMasukDetailRequest(id=int(id))
        response = self.stub.get(request)
        
        if response is None:
            return None
        
        return dict(
            id = response.barangmasuk.id,
            item = response.barangmasuk.item,
            tanggalMasuk = response.barangmasuk.tanggalMasuk,
            supplierID = response.barangmasuk.supplierID,
            qty = response.barangmasuk.qty,
        )
    
    def create_barangmasuk(self, item, tanggalMasuk, supplierID, qty):
        request = barangkeluar_pb2.BarangMasukCreateRequest(
            item=item,
            tanggalMasuk=tanggalMasuk,
            supplierID=supplierID,
            qty=int(qty),
        )
        response = self.stub.create(request)
        
        if response is None:
            return None
        
        return dict(
            id = response.barangmasuk.id,
            item = response.barangmasuk.item,
            tanggalMasuk = response.barangmasuk.tanggalMasuk,
            supplierID = response.barangmasuk.supplierID,
            qty = response.barangmasuk.qty,
        )
    
    def update_barangmasuk(self, id, item, tanggalMasuk, supplierID, qty):
        request = barangkeluar_pb2.BarangMasukUpdateRequest(
            id=int(id),
            item=item,
            tanggalMasuk=tanggalMasuk,
            supplierID=supplierID,
            qty=int(qty),
        )
        response = self.stub.update(request)
        
        if response is None:
            return None
        
        return dict(
            id = response.barangmasuk.id,
            item = response.barangmasuk.item,
            tanggalMasuk = response.barangmasuk.tanggalMasuk,
            supplierID = response.barangmasuk.supplierID,
            qty = response.barangmasuk.qty,
            message="BarangMasuk updated successfully"
        )
    
    def delete_barangmasuk(self, id):
        request = barangkeluar_pb2.BarangMasukDeleteRequest(id=int(id))
        response = self.stub.delete(request)
        
        if response is None:
            return None
        
        return dict(
            message = "BarangMasuk deleted successfully"
        )

            