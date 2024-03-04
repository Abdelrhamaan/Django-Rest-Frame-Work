const getForm = document.getElementById("login-form");
let getContainer = document.getElementById("container");
console.log(getContainer);
let baseEndPoint = "http://localhost:8000/api";

// Check for existing token when the page loads
document.addEventListener("DOMContentLoaded", function () {
  const accessToken = localStorage.getItem("accessToken");
  if (accessToken) {
    handleProducts();
  } else {
    window.location.href = "http://localhost:8111/"; // Redirect to login page if no token
  }
});

if (baseEndPoint) {
  getForm.addEventListener("submit", handleLogin);
}

async function handleLogin(e) {
  console.log(e);
  e.preventDefault();
  let baseUrl = `${baseEndPoint}/token/`;
  let loginForm = new FormData(getForm);
  let formData = Object.fromEntries(loginForm);
  console.log(formData);
  let cerdentials = JSON.stringify(formData);
  let options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: cerdentials,
  };

  try {
    const response = await fetch(baseUrl, options);
    const data = await response.json();
    console.log(data);
    saveTokens(data, handleProducts);
  } catch (e) {
    console.log(e);
  }
}

function saveTokens(data, callback) {
  localStorage.setItem("accessToken", data.access);
  localStorage.setItem("refreshToken", data.refresh);
  if (callback) {
    callback();
  }
}

function getOptions(method, body) {
  return (options = {
    method: method === null ? "GET" : method,
    headers: {
      "content-type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
    },
    body: body ? body : null,
  });
}

async function getNewAccessToken() {
  let refreshToken = localStorage.getItem("refreshToken");
  let endPoint = `${baseEndPoint}/token/refresh/`;
  const options = {
    method: "POST",
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify({ refresh: refreshToken }),
  };

  try {
    const response = await fetch(endPoint, options);
    const data = await response.json();
    saveTokens(data, handleProducts);
  } catch (error) {
    console.error("Error refreshing token:", error);
    // Handle error, maybe redirect to login page
    window.location.href = "http://localhost:8111/";
  }
}

async function isTokenExpired(token) {
  if (!token) {
    return true;
  }
  const decodedToken = jwt_decode(token);
  const currentTime = Date.now() / 1000;
  return decodedToken.exp < currentTime;
}

async function isNotValidToken(res) {
  if (res.code && res.code === "token_not_valid") {
    console.log("Token expired, refreshing...");
    const accessTokenExpired = await isTokenExpired(
      localStorage.getItem("accessToken")
    );
    const refreshTokenExpired = await isTokenExpired(
      localStorage.getItem("refreshToken")
    );
    if (accessTokenExpired && refreshTokenExpired) {
      console.log("Both tokens expired, redirecting to login...");
      window.location.href = "http://localhost:8111/";
      return false;
    } else {
      await getNewAccessToken();
    }
  }
  return true;
}

function writeData(data) {
  if (getContainer) {
    console.log("in if");
    getContainer.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "</pre>";
  }
}

async function handleProducts() {
  let baseUrl = `${baseEndPoint}/products/`;
  console.log(localStorage.getItem("accessToken"));

  let options = getOptions();

  try {
    const response = await fetch(baseUrl, options);
    const data = await response.json();
    console.log(data);
    isValidData = await isNotValidToken(data);
    if (isValidData) {
      writeData(data);
    }
  } catch (e) {
    console.log(e);
  }
}
