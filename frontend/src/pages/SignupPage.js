
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { Form, Button, Container, Row, Col, Alert, Spinner } from "react-bootstrap";
import "./SignupPage.css"; // Custom CSS for ASU styling

const SignupPage = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState("");
  const navigate = useNavigate();

  const handleSignup = (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");

    axios
      .post("/auth/signup", { username, password }, {
        headers: { "Content-Type": "application/json" },
      })
      .then((response) => {
        setSuccess("Signup successful! Redirecting to login...");
        setTimeout(() => navigate("/login"), 2000);
      })
      .catch((error) => {
        if (error.response) {
          setError(error.response.data.message);
        } else {
          setError("An error occurred. Please try again.");
        }
      })
      .finally(() => {
        setLoading(false);
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
        <h2 className="text-center mb-4">Create an Account</h2>
        <Form onSubmit={handleSignup}>
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
            <Button variant="primary" type="submit" disabled={loading}>
              {loading ? <Spinner animation="border" size="sm" /> : "Sign Up"}
            </Button>
          </div>
        </Form>
        {error && <Alert variant="danger" className="mt-3">{error}</Alert>}
        {success && <Alert variant="success" className="mt-3">{success}</Alert>}
        <p className="text-center mt-3">
          Already have an account? <a href="/login">Log in here</a>.
        </p>
      </div>
    </Col>
  </Row>
</Container>

  );
};

export default SignupPage;
