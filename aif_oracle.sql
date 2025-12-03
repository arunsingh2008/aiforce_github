CREATE TABLE salesforce_tasks (
    id NUMBER PRIMARY KEY,
    subject VARCHAR2(255),
    status VARCHAR2(50),
    priority VARCHAR2(50),
    description CLOB,
    created_date DATE,
    due_date DATE
);

CREATE INDEX idx_salesforce_tasks_status ON salesforce_tasks(status);
CREATE INDEX idx_salesforce_tasks_priority ON salesforce_tasks(priority);