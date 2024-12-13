import React, { useEffect, useState } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import { Container, Row, Col, Card, Badge, Nav, Navbar } from "react-bootstrap";
import { NavLink } from "react-router-dom";
import "./StudentPage.css";



const StudentPage = () => {
  const [student, setStudent] = useState(null);

  useEffect(() => {
    axios
      .get("/api/student", { withCredentials: true })
      .then((response) => {
        console.log('Student data:', response.data);
        setStudent(response.data);
      })
      .catch((error) => console.error("Error fetching student data:", error));
  }, []);

  if (!student) {
    return <div className="loading">Loading...</div>;
  }

  return (
    <>
      {/* Navigation Bar */}
                <Navbar expand="lg" className="navbar-asu shadow-sm">
            <Container>
              <Navbar.Brand className="navbar-brand">
                AchievementHub
              </Navbar.Brand>
              <Navbar.Toggle aria-controls="navbarNav" />
              <Navbar.Collapse id="navbarNav">
                <Nav className="ms-auto">
                  <Nav.Link
                    as={NavLink}
                    to="/badges"
                    className="nav-link-asu"
                  >
                    My Badges
                  </Nav.Link>
                  <Nav.Link
                    as={NavLink}
                    to="/"
                    className="nav-link-asu"
                  >
                    Logout
                  </Nav.Link>
                </Nav>
              </Navbar.Collapse>
            </Container>
          </Navbar>

      {/* Student Info Section */}
      <Container className="mt-5">
        <div className="text-center student-info">
          <h1 className="fw-bold asu-maroon">Welcome, {student.name}</h1>
          <div className="d-flex justify-content-center align-items-center mt-4">
            <img
              src='/images/pic.png'
              alt="Profile"
              className="rounded-circle me-3"
              width="100"
              height="100"
            />
            {/* <div>
              <h4 className="mb-1">{student.grade}</h4>
              <p className="text-muted">
                Keep achieving and growing your streaks!
              </p>
            </div> */}
          </div>
          <div className="mt-3">
            <Badge className="bg-asu-gold me-2">
              {/* Current Streak: {student.current_streak} days */}
            </Badge>
            <Badge className="bg-asu-turquoise">
              {/* Longest Streak: {student.longest_streak} days */}
            </Badge>
          </div>
        </div>

        {/* Badges Section */}
        <h2 className="mt-5 mb-4 text-center asu-maroon">
        
        </h2>
        <Row>
          {student.badges.map((badge, index) => (
            <Col md={4} className="mb-4" key={index}>
              <Card className="h-100 badge-card">
                <Card.Img
                  variant="top"
                  src={`http://127.0.0.1:5000${badge.image}`}
                  alt={badge.title}
                  className="badge-image"
                />
                <Card.Body className="text-center">
                  <Card.Title className="asu-maroon badge-card-title">
                    {badge.title}
                  </Card.Title>
                  <Card.Text className="badge-card-text">
                    {badge.description}
                  </Card.Text>
                </Card.Body>
               
              </Card>
            </Col>
          ))}
        </Row>
      </Container>
    </>
  );
};

export default StudentPage;
