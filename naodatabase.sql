use naodatabase;

CREATE TABLE inventario(
ID int not null AUTO_INCREMENT primary key,
CODIGO int not null,
ARTICULO VARCHAR(50) not null,
CANTIDAD VARCHAR(50) not null,
IMPORTE VARCHAR(50) not null,
SALDO VARCHAR(50) not null,
CANT_HOY VARCHAR(50) not null,
CANT_ANT VARCHAR(50) not null,
IMPORT_ANT VARCHAR(50) not null,
FALTANTE VARCHAR(50) not null,
FISICO VARCHAR(50) not null
)

select * from inventario;



