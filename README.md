# EveryKnowAPI

Backend for knowledge base of Everyday IT crowd

Запустить сервер: 

uvicorn main:app --reload

Перейти по адресу

http://127.0.0.1:8000/docs

Структура базы данных на данный момент вижу таким:

```SQL
CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100)
);

CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(100),
    ParentCategoryID INT,
    FOREIGN KEY (ParentCategoryID) REFERENCES Categories(CategoryID)
);

CREATE TABLE Articles (
    ArticleID INT PRIMARY KEY,
    Title VARCHAR(200),
    Content TEXT,
    CreatedDate DATETIME,
    LastModifiedDate DATETIME,
    AuthorID INT,
    CategoryID INT,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);

CREATE TABLE Tags (
    TagID INT PRIMARY KEY,
    TagName VARCHAR(50)
);

CREATE TABLE ArticleTags (
    ArticleID INT,
    TagID INT,
    PRIMARY KEY (ArticleID, TagID),
    FOREIGN KEY (ArticleID) REFERENCES Articles(ArticleID),
    FOREIGN KEY (TagID) REFERENCES Tags(TagID)
);

CREATE TABLE Comments (
    CommentID INT PRIMARY KEY,
    ArticleID INT,
    AuthorID INT,
    Content TEXT,
    CreatedDate DATETIME,
    FOREIGN KEY (ArticleID) REFERENCES Articles(ArticleID),
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);
```