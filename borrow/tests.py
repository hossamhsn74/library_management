import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from borrow.models import Book, BorrowRecord


@pytest.fixture
def api_client():
    """
    Fixture to create an API client.
    """
    return APIClient()


@pytest.fixture
def user():
    """
    Fixture to create a test user.
    """
    return User.objects.create_user(username='testuser', password='testpassword')


@pytest.fixture
def token(user):
    """
    Fixture to create a token for the test user.
    """
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


@pytest.fixture
def authenticated_client(api_client, token):
    """
    Fixture to create an authenticated client.
    """
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
    return api_client


@pytest.fixture
def book():
    """
    Fixture to create a test book.
    """
    return Book.objects.create(title='Test Book', available=True)


@pytest.fixture
def borrow_record(user, book):
    """
    Fixture to create a test borrow record.
    """
    return BorrowRecord.objects.create(book=book, borrower=user)


@pytest.mark.django_db
def test_list_books(authenticated_client, book):
    """
    Test to list all books.
    """
    url = reverse('book-list')
    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


@pytest.mark.django_db
def test_create_book(authenticated_client, user):
    """
    Test to create a new book.
    """
    url = reverse('book-list')
    data = {'title': 'New Book', 'author': user.id, 'available': True}
    response = authenticated_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_retrieve_book(authenticated_client, book):
    """
    Test to retrieve a book.
    """
    url = reverse('book-detail', args=[book.id])
    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == book.title


@pytest.mark.django_db
def test_update_book(authenticated_client, user, book):
    """
    Test to update a book.
    """
    url = reverse('book-detail', args=[book.id])
    data = {'title': 'Updated Book', 'author': user.id, 'available': False}
    response = authenticated_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == 'Updated Book'
    assert response.data['available'] is False


@pytest.mark.django_db
def test_delete_book(authenticated_client, book):
    """
    Test to delete a book.
    """
    url = reverse('book-detail', args=[book.id])
    response = authenticated_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_borrow_book(authenticated_client, user, book):
    """
    Test to borrow a book.
    """
    url = reverse('borrowrecord-list')
    data = {'book': book.id, 'borrower': user.id}
    response = authenticated_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    book.refresh_from_db()
    assert not book.available


@pytest.mark.django_db
def test_return_book(authenticated_client, borrow_record):
    """
    Test to return a borrowed book.
    """
    url = reverse('borrowrecord-detail', args=[borrow_record.id])
    data = {
        'book': borrow_record.book.id,
        'borrower': borrow_record.borrower.id,
        'borrow_date': borrow_record.borrow_date,
        'return_date': '2024-07-23'
    }
    response = authenticated_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    borrow_record.book.refresh_from_db()
    assert borrow_record.book.available


@pytest.mark.django_db
def test_get_borrow_record_list(authenticated_client, borrow_record):
    """
    Test to list all borrow records.
    """
    url = reverse('borrowrecord-list')
    response = authenticated_client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


@pytest.mark.django_db
def test_get_borrow_record_detail(authenticated_client, borrow_record):
    """
    Test to retrieve a borrow record.
    """
    url = reverse('borrowrecord-detail', args=[borrow_record.id])
    response = authenticated_client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == borrow_record.id


@pytest.mark.django_db
def test_update_borrow_record(authenticated_client, borrow_record):
    """
    Test to update a borrow record.
    """
    url = reverse('borrowrecord-detail', args=[borrow_record.id])
    data = {
        'book': borrow_record.book.id,
        'borrower': borrow_record.borrower.id,
        'borrow_date': borrow_record.borrow_date.strftime('%Y-%m-%d'),
        'return_date': '2024-07-23'
    }
    response = authenticated_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    borrow_record.refresh_from_db()
    assert borrow_record.return_date.strftime('%Y-%m-%d') == '2024-07-23'


@pytest.mark.django_db
def test_delete_borrow_record(authenticated_client, borrow_record):
    """
    Test to delete a borrow record.
    """
    url = reverse('borrowrecord-detail', args=[borrow_record.id])
    response = authenticated_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
