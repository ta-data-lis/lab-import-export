SELECT * FROM customer;

SELECT customer.customer_id, customer.first_name, customer.last_name, rental.rental_id, rental.rental_date, rental.return_date
FROM customer
JOIN rental ON customer.customer_id = rental.customer_id;

SELECT * 
FROM actor
INNER JOIN film_actor
ON film_actor.actor_id = actor.actor_id
INNER JOIN film
ON film.film_id = film_actor.film_id;