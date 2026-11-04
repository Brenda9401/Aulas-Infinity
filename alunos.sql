CREATE TABLE alunos (
	id INT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT
    
);

INSERT INTO alunos(id, nome, idade) VALUES 
	(1, "Brenda", 32),
    (2, "Ricardo", 24),
    (3, "Gabriel", 29);
    
SELECT * FROM alunos;
