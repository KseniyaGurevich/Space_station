import pytest
from rest_framework import status

from .models import Station, User


@pytest.fixture
def test_station():
    """Создает станцию"""
    Station.objects.create(name="First")


@pytest.fixture
def api_client():
    """Возвращает APIClient для создания запросов."""
    from rest_framework.test import APIClient
    return APIClient()

@pytest.fixture
def auth_user(api_client):
    """Создание и аутентификация пользователя"""
    user = User.objects.create(username='user_1', password='password_1')
    return api_client.force_authenticate(user=user)


@pytest.mark.django_db
class TestStation:
    @pytest.mark.usefixtures("test_station")
    def test_create_station(self):
        stations = Station.objects.all()
        single_station = stations.filter(name="First")
        assert stations.count() == 1, 'В бд должны быть всего одна станция'
        assert single_station[0].x == 100, 'При запуске станции по умолчанию х = 100'
        assert single_station[0].y == 100, 'При запуске станции по умолчанию y = 100'
        assert single_station[0].z == 100, 'При запуске станции по умолчанию y = 100'
        assert single_station[0].state == 'running', 'При запуске станция по умолчанию рабочая'
        assert single_station[0].date_broken is None, 'Графа "Дата поломки" должна быть пустой'
        assert single_station[0].date_creation is not None, ('Графа "Дата создания" станции'
                                                             ' должна быть заполнена по умолчанию')

    @pytest.mark.usefixtures("test_station", "auth_user")
    def test_create_instruction_x(self, api_client):
        """Инструкции для станции"""
        station = Station.objects.filter(name="First")[0]
        # user = User.objects.create(username='user_1', password='password_1')
        # api_client.force_authenticate(user=user)
        station_list = api_client.get('/stations/', format='api')
        instruction_1 = api_client.post(
            f'/stations/{station.id}/state/',
            {'user': 'user_1', 'axis': 'x', 'distance': -500},
            format='json'
        )
        coord_1 = api_client.get(
            f'/stations/{station.id}/state/',
            format='json'
        )
        station_1 = Station.objects.filter(name="First")[0]
        instruction_2 = api_client.post(
            f'/stations/{station.id}/state/',
            {'user': 'user_1', 'axis': 'x', 'distance': 666},
            format='json'
        )
        coord_2 = api_client.get(
            f'/stations/{station.id}/state/',
            format='json'
        )
        station_2 = Station.objects.filter(name="First")[0]
        assert station_list.status_code == status.HTTP_200_OK
        assert instruction_1.status_code == status.HTTP_201_CREATED
        assert coord_1.json()['x'] == -400, "Координата x должна быть равна -400"
        assert coord_1.json()['x'] == station_1.x, "Координата x после указания_1 не соответсвует ответу сериалайзера"
        assert coord_1.json()['y'] == station_1.y, "Координата y после указания_1 не соответсвует ответу сериалайзера"
        assert coord_1.json()['z'] == station_1.z, "Координата z после указания_1 не соответсвует ответу сериалайзера"
        assert station.state == 'running', "До указаний станция должна быть исправна"
        assert station_1.state == 'broken', "После укзания_1 станция должна быть сломана"
        assert instruction_2.status_code == status.HTTP_201_CREATED
        assert coord_2.json()['x'] == 266, "Координата x должна быть равна 266"
        assert coord_2.json()['x'] == station_2.x, "Координата х после указания_2 не соответсвует ответу сериалайзера"
        assert coord_2.json()['y'] == station_2.y, "Координата y после указания_2 не соответсвует ответу сериалайзера"
        assert coord_2.json()['z'] == station_2.z, "Координата z после указания_2 не соответсвует ответу сериалайзера"
        assert station_2.state == 'broken', "После укзания_2 станция также должна быть сломана"
        assert station_1.date_broken == station_2.date_broken, ("Время поломки после первого указания и после второго "
                                                                "должно быть одинаковое")

    @pytest.mark.usefixtures("test_station", "auth_user")
    def test_create_instruction_y(self, api_client):
        """Поломка станции при y < 0"""
        station = Station.objects.filter(name="First")[0]
        instruction_1 = api_client.post(
            f'/stations/{station.id}/state/',
            {'user': 'user_1', 'axis': 'y', 'distance': -500},
            format='json'
        )
        coord_1 = api_client.get(
            f'/stations/{station.id}/state/',
            format='json'
        )
        station_1 = Station.objects.filter(name="First")[0]
        instruction_2 = api_client.post(
            f'/stations/{station.id}/state/',
            {'user': 'user_1', 'axis': 'y', 'distance': 666},
            format='json'
        )
        coord_2 = api_client.get(
            f'/stations/{station.id}/state/',
            format='json'
        )
        station_2 = Station.objects.filter(name="First")[0]
        assert coord_1.json()['y'] == -400, "Координата y после сдвига ее на -500 должна быть равна -400"
        assert coord_2.json()['y'] == 266, "Координата y после сдвига ее на 666 должна быть равна 266"
        assert station_1.state == 'broken', "После укзания_1 станция должна быть сломана"
        assert station_2.state == 'broken', "После укзания_2 станция также должна быть сломана"
        assert station_1.date_broken == station_2.date_broken, ("Время поломки после первого указания и "
                                                                "после второго должно быть одинаковое")

    @pytest.mark.usefixtures("test_station", "auth_user")
    def test_create_instruction_z(self, api_client):
        """Поломка станции при y < 0"""
        station = Station.objects.filter(name="First")[0]
        instruction_1 = api_client.post(
            f'/stations/{station.id}/state/',
            {'user': 'user_1', 'axis': 'z', 'distance': -500},
            format='json'
        )
        coord_1 = api_client.get(
            f'/stations/{station.id}/state/',
            format='json'
        )
        station_1 = Station.objects.filter(name="First")[0]
        instruction_2 = api_client.post(
            f'/stations/{station.id}/state/',
            {'user': 'user_1', 'axis': 'z', 'distance': 666},
            format='json'
        )
        coord_2 = api_client.get(
            f'/stations/{station.id}/state/',
            format='json'
        )
        station_2 = Station.objects.filter(name="First")[0]
        assert coord_1.json()['z'] == -400, "Координата z после сдвига ее на -500 должна быть равна -400"
        assert coord_2.json()['z'] == 266, "Координата z после сдвига ее на 666 должна быть равна 266"
        assert station_1.state == 'broken', "После укзания_1 станция должна быть сломана"
        assert station_2.state == 'broken', "После укзания_2 станция также должна быть сломана"
        assert station_1.date_broken == station_2.date_broken, ("Время поломки после первого указания и "
                                                                "после второго должно быть одинаковое")


