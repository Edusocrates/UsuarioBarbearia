from adapter.repository.AgendaRepository import AgendaRepository
from adapter.controller.inbound.dto.CriaAgendaDTO import CriaAgendaDTO


class AgendaService:
    @staticmethod
    def obter_todos_agendamentos():
        return AgendaRepository.obter_todos_agendamentos()

    @staticmethod
    def criar_agendamento(nome_cliente, data_agendamento, servico, nome_profissional):
        return AgendaRepository.criar_agendamento(nome_cliente, data_agendamento, servico, nome_profissional)