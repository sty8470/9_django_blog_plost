# Blog Post CRUD API

This project provides a CRUD API for managing blog posts using a single `blog_post` table.

## Table Structure

- **id**: Integer, primary key, auto-incremented
- **name**: String, author name
- **title**: String, post title
- **contents**: Text, post contents
- **created_at**: DateTime, creation timestamp
- **updated_at**: DateTime, last update timestamp

## Endpoints

### Retrieve Blog Posts

**GET /english-cafe/posts/?page=1**

Fetches a paginated list of blog posts. The `page` parameter is optional and defaults to the first page.

**Response:**

- **total_count**: Total number of blog posts
- **count**: Number of blog posts in the current page
- **prev_page**: URL of the previous page
- **next_page**: URL of the next page
- **results**: List of blog posts

---

### Create a Blog Post

**POST /english-cafe/posts/**

Creates a new blog post.

**Request Payload:**

- **name**: Author name
- **title**: Post title
- **contents**: Post contents

**Response:**

- **id**: Blog post ID
- **name**: Author name
- **title**: Post title
- **contents**: Post contents
- **created_at**: Creation timestamp
- **updated_at**: Last update timestamp

---

### Update a Blog Post

**PUT /english-cafe/posts/{id}/**

Updates an existing blog post.

**Request Payload:**

- **name**: Author name
- **title**: Post title
- **contents**: Post contents

**Response:**

- **id**: Blog post ID
- **name**: Author name
- **title**: Post title
- **contents**: Post contents
- **created_at**: Creation timestamp
- **updated_at**: Last update timestamp

---

### Delete a Blog Post

**DELETE /english-cafe/posts/{id}/**

Deletes a blog post by ID.

**Response:**

- None

---

## Conclusion

This API provides essential CRUD operations for managing blog posts with a simple and efficient design.