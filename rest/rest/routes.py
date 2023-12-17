def includeme(config):
    config.add_route("home", "/")
    config.add_route("item", "/api/v1/item{action:.*}")
    config.add_route("kategori", "/api/v1/kategori{action:.*}")
    config.add_route("rack", "/api/v1/rack{action:.*}")
    config.add_route("role", "/api/v1/role{action:.*}")
    # config.add_route("login-anggota", "/api/v1/login-anggota")
    # config.add_route("logout-anggota", "/api/v1/logout-anggota")
    
    # config.add_route("kategori", "/api/v1/kategori{action:.*}")
    # config.add_route("petugas", "/api/v1/petugas{action:.*}")
    # config.add_route("petugas_login", "/api/v1/login-petugas")
    # config.add_route("petugas_logout", "/api/v1/logout-petugas")
    # config.add_route("peminjaman", "/api/v1/peminjaman{action:.*}")
