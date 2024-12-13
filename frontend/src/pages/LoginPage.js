
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { Form, Button, Container, Row, Col, Alert } from "react-bootstrap";
import "./LoginPage.css"; // Import ASU-styled CSS

const LoginPage = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    axios
      .post(
        "/auth/login",
        { username, password }, // Request payload
        {
          withCredentials: true, // Include credentials for session-based authentication
          headers: { "Content-Type": "application/json" }, // Explicit Content-Type
        }
      )
      .then((response) => {
        console.log(response.data);
        navigate("/students"); // Redirect to student page on successful login
      })
      .catch((error) => {
        if (error.response) {
          setError(error.response.data.message);
        } else {
          setError("An error occurred. Please try again.");
        }
      });
  };

  return (
    <Container fluid className="vh-100 d-flex align-items-center justify-content-center">
    <Row className="w-100">
      {/* Left Half */}
      <Col md={6} className="d-flex align-items-center justify-content-center ">
        <div className="text-center">
          <img
            src="/images/Learn.png"
            alt="Learn to Thrive"
            className="img-fluid"
            style={{ maxWidth: "80%" }}
          />
         
        </div>
      </Col>
  
      {/* Right Half */}

<Col md={6} className="d-flex align-items-center justify-content-center">
  <div className="p-4 w-75">
  <h2 className="text-center mb-4">Login</h2>
    
    <Form onSubmit={handleLogin}>
      <Form.Group className="mb-3" controlId="username">
      <Form.Label>Username</Form.Label>
        <Form.Control
          type="text"
         
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
      </Form.Group>
      <Form.Group className="mb-3" controlId="password">
      <Form.Label>Password</Form.Label>
        <Form.Control
          type="password"
          
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
      </Form.Group>
      <div className="d-grid">
        <Button variant="primary" type="submit">
          Login
        </Button>
      </div>
    </Form>
    {error && <Alert variant="danger" className="mt-3">{error}</Alert>}
    <p className="text-center mt-3">
      Reset or SignUp <a href="/signup">click here</a>.
    </p>
  </div>
</Col>

    </Row>
  </Container>
  
  
  );
};

export default LoginPage;

