import heapq

class LCG:
    def __init__(self, seed=1):
        self.m = 2**31
        self.a = 1103515245
        self.c = 12345
        self.state = seed
        self.count = 0

    def random(self):
        self.state = (self.a * self.state + self.c) % self.m
        self.count += 1
        return self.state / self.m

    def uniform(self, a, b):
        return a + self.random() * (b - a)


class Fila:
    def __init__(self, id, servidores, capacidade,
                 servico_min, servico_max,
                 chegada_min=None, chegada_max=None):

        self.id = id
        self.servidores = servidores
        self.capacidade = capacidade
        self.servico_min = servico_min
        self.servico_max = servico_max
        self.chegada_min = chegada_min
        self.chegada_max = chegada_max

        self.no_sistema = 0
        self.em_servico = 0
        self.perdas = 0
        self.acumulado = [0.0] * (capacidade + 1)


class Simulador:
    CHEGADA = 0
    SAIDA = 1

    def __init__(self):
        self.rng = LCG(seed=1)
        self.limite = 100000
        self.tempo = 0.0
        self.eventos = []

        # Configuração das filas
        self.filas = {
            1: Fila(
                id=1,
                servidores=2,
                capacidade=3,
                chegada_min=1,
                chegada_max=4,
                servico_min=3,
                servico_max=4
            ),
            2: Fila(
                id=2,
                servidores=1,
                capacidade=5,
                servico_min=2,
                servico_max=3
            )
        }

        # Roteamento: Fila 1 -> Fila 2 -> Saída
        self.roteamento = {
            1: 2,
            2: None
        }

        self.tempo_primeira_chegada = 1.5


    def agendar(self, tempo, tipo, fila_id):
        heapq.heappush(self.eventos, (tempo, tipo, fila_id))

    def atualizar_estatisticas(self, novo_tempo):
        delta = novo_tempo - self.tempo
        for fila in self.filas.values():
            fila.acumulado[fila.no_sistema] += delta
        self.tempo = novo_tempo


    def chegada(self, fila_id, externa=False):
        fila = self.filas[fila_id]

        # Agenda próxima chegada externa apenas para a Fila 1
        if externa and self.rng.count < self.limite:
            intervalo = self.rng.uniform(
                fila.chegada_min, fila.chegada_max
            )
            self.agendar(
                self.tempo + intervalo,
                self.CHEGADA,
                fila_id
            )

        # Verifica capacidade
        if fila.no_sistema >= fila.capacidade:
            fila.perdas += 1
            return

        fila.no_sistema += 1

        # Inicia atendimento se houver servidor livre
        if fila.em_servico < fila.servidores:
            fila.em_servico += 1
            if self.rng.count < self.limite:
                tempo_servico = self.rng.uniform(
                    fila.servico_min,
                    fila.servico_max
                )
                self.agendar(
                    self.tempo + tempo_servico,
                    self.SAIDA,
                    fila_id
                )

    def saida(self, fila_id):
        fila = self.filas[fila_id]

        fila.no_sistema -= 1
        fila.em_servico -= 1

        # Inicia atendimento do próximo cliente
        if fila.no_sistema >= fila.servidores:
            fila.em_servico += 1
            if self.rng.count < self.limite:
                tempo_servico = self.rng.uniform(
                    fila.servico_min,
                    fila.servico_max
                )
                self.agendar(
                    self.tempo + tempo_servico,
                    self.SAIDA,
                    fila_id
                )

        # Roteamento para a próxima fila
        destino = self.roteamento[fila_id]
        if destino is not None:
            self.chegada(destino, externa=False)


    def executar(self):
        # Agenda a primeira chegada na Fila 1
        self.agendar(
            self.tempo_primeira_chegada,
            self.CHEGADA,
            1
        )

        while self.eventos and self.rng.count < self.limite:
            tempo, tipo, fila_id = heapq.heappop(self.eventos)
            self.atualizar_estatisticas(tempo)

            if tipo == self.CHEGADA:
                self.chegada(fila_id, externa=(fila_id == 1))
            else:
                self.saida(fila_id)

        self.salvar_resultados()


    def salvar_resultados(self):
        linhas = []
        linhas.append("=" * 58)

        for fila in self.filas.values():
            linhas.append(f"Fila {fila.id}")
            linhas.append("-" * 58)
            linhas.append(
                "Estado | Tempo Acumulado | Probabilidade"
            )

            for estado, tempo in enumerate(fila.acumulado):
                prob = tempo / self.tempo if self.tempo > 0 else 0
                linhas.append(
                    f"{estado:^6} | {tempo:>17.4f} | {prob:>14.6f}"
                )

            linhas.append("-" * 58)
            linhas.append(f"Perdas: {fila.perdas}\n")

        linhas.append(f"Tempo Global: {self.tempo:.4f}")
        linhas.append(
            f"Números Aleatórios Utilizados: {self.rng.count}"
        )
        linhas.append("=" * 58)

        resultado = "\n".join(linhas)

        with open("resposta.txt", "w", encoding="utf-8") as f:
            f.write(resultado)

        print(resultado)
        print("\nArquivo 'resposta.txt' gerado com sucesso!")


# ======================================================
# PROGRAMA PRINCIPAL
# ======================================================
if __name__ == "__main__":
    simulador = Simulador()
    simulador.executar()
