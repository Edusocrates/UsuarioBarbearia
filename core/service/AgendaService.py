from adapter.repository.AgendaRepository import AgendaRepository
from adapter.controller.inbound.dto.CriaAgendaDTO import CriaAgendaDTO


class AgendaService:
    @staticmethod
    def obter_todos_agendamentos():
        return AgendaRepository.obter_todos_agendamentos()

    @staticmethod
    def criar_agendamento(criar_agendamento):
        return AgendaRepository.criar_agendamento(criar_agendamento.nome_cliente, criar_agendamento.data_agendamento, criar_agendamento.servico, criar_agendamento.nome_profissional)